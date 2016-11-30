import React, { PropTypes } from 'react'
import { Link } from 'react-router'

const service = ({ service }) => {
  const { title, description } = service

  return (
    <div className="Service">
      <h3>
        <Link to={`ismaell/ismael`}>
          {title}
        </Link>
        {' by '}
        <Link to={`/ismael`}>
          {login}
        </Link>
      </h3>
      {description &&
        <p>{description}</p>
      }
    </div>
  )
}

Repo.propTypes = {
  repo: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string
  }).isRequired
}

export default Repo
